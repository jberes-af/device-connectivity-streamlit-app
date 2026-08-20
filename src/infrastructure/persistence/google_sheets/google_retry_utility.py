# infrastructure/persistence/google_sheets/google_retry_utility.py

import random
from time import sleep
from typing import Callable, TypeVar

import httplib2
from googleapiclient.errors import HttpError

T = TypeVar("T")


def retry_google_api_operation(
        operation: Callable[[], T],
        *,
        max_attempts: int = 5,
        initial_delay_s: float = 1.0,
        max_delay_s: float = 32.0,
        on_retry: Callable[[int, float, Exception], None] | None = None,
) -> T:
    """
    Retry transient Google API and network errors
    using exponential backoff with jitter.

    max_attempts includes the initial attempt.
    """

    delay = initial_delay_s

    for attempt in range(1, max_attempts + 1):
        try:
            return operation()

        except HttpError as err:
            status = getattr(err.resp, "status", None)
            message = str(err)

            transient = (
                    status in (429, 500, 502, 503, 504)
                    or (
                            status == 403
                            and "rateLimitExceeded" in message
                    )
                    or (
                            status == 403
                            and "userRateLimitExceeded" in message
                    )
            )

            if not transient or attempt == max_attempts:
                raise

            sleep_time = _calculate_backoff(
                delay=delay,
                max_delay_s=max_delay_s,
            )

            if on_retry:
                on_retry(
                    attempt,
                    sleep_time,
                    err,
                )

            sleep(sleep_time)
            delay = min(delay * 2, max_delay_s)

        except (
                TimeoutError,
                TimeoutError,
                httplib2.HttpLib2Error,
                ConnectionError,
        ) as err:
            if attempt == max_attempts:
                raise

            sleep_time = _calculate_backoff(
                delay=delay,
                max_delay_s=max_delay_s,
            )

            if on_retry:
                on_retry(
                    attempt,
                    sleep_time,
                    err,
                )

            sleep(sleep_time)
            delay = min(delay * 2, max_delay_s)


def _calculate_backoff(
        *,
        delay: float,
        max_delay_s: float,
) -> float:
    jitter = random.uniform(0.5, 1.5)

    return min(
        delay * jitter,
        max_delay_s,
    )
