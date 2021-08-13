from datetime import datetime
from typing import Tuple

import jwt

from core.config import ACCESS_TOKEN_EXP_DELTA
from core.env import environment


def get_access_refresh_token(session, payload) -> Tuple[str, str]:
    """Generate access_token & refresh token.
    access tokens are stateless JWTs
    refresh tokens are stored in the database
    """
    now = datetime.now()
    message = {
        'exp': now + ACCESS_TOKEN_EXP_DELTA,
        'created_at': now.timestamp(),
        **payload,
    }
    access = jwt.encode(message, environment.secret_key, algorithm="HS256")
    # refresh_token = RefreshTokensCRUD.create(session=session, user_id=user.id)
    # session.flush()
    return access, "refresh_token.token"
