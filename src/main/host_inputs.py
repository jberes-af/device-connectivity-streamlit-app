# /src/main/host_inputs.py

from src.domain.enums.person.tenant_enums import UserRoleEnum

from src.application.context import SessionContext, UserContext

# SessionContext(user_context=UserContext(user_id='1hB6CrpvpgMzQ5KF6v0igsAROFa2', tenant_id='cbaac9b44af248b18f4833494f042c3b', role=<UserRoleEnum.ADMINISTRATOR: 'Administrator'>))


from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class HostInputs:
    bypass_authentication: bool
    session_context: SessionContext


def load_host_inputs() -> HostInputs:
    return HostInputs(
        bypass_authentication=True,
        session_context=SessionContext(
            user_context=UserContext(
                user_id="FlEl9LLqpBcFX7xyLcE8OYfTvZ73",  # living well
                tenant_id="b77891d5e60d40789698e8a9d4187fe9",
                # role=UserRoleEnum.ADMINISTRATOR,
                role=UserRoleEnum.OWNER,
            )

        ),
    )
