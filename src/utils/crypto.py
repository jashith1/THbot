import hashlib
import json
import hmac
import time
from fastapi import Request

from src.exceptions.custom_exceptions import Unauthorized
from src.utils.config import settings

async def verify_hmac(request: Request):
    if settings.ENV == "development":
        return

    request_hmac = request.headers.get("x-authorization-content-hmac")
    request_timestamp = request.headers.get("x-authorization-timestamp")

    if not request_hmac:
        raise Unauthorized("Missing HMAC signature header")

    if not request_timestamp:
        raise Unauthorized("Missing HMAC timestamp header")

    # make sure request is not older than 5 min
    if abs(time.time() - float(request_timestamp)) > 300:
        raise Unauthorized("Provided HMAC timestamp is either too old or invalid")

    request_body_raw = await request.body()
    request_body = request_body_raw.decode("utf-8")
    msg = f"{request_timestamp}{request_body}".encode("utf-8")

    new_hmac = hmac.new(
        key=settings.HMAC_SECRET.encode("utf-8"), msg=msg, digestmod=hashlib.sha256
    ).hexdigest()

    if not hmac.compare_digest(request_hmac, new_hmac):
        raise Unauthorized("HMAC Signature Does not match")


def create_hmac(data: dict):
    #TODO: look into if keys should be sorted?
    print("creating")
    json_payload = json.dumps(data, separators=(',', ':'))
    hmac_timestamp = time.time()
    msg = f"{hmac_timestamp}{json_payload}".encode("utf-8")

    hmac_signature = hmac.new(
        key=settings.HMAC_SECRET.encode("utf-8"), msg=msg, digestmod=hashlib.sha256
    ).hexdigest()

    return { "x-authorization-timestamp": str(hmac_timestamp), "x-authorization-content-hmac": hmac_signature }

