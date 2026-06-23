from fastapi import Depends, HTTPException, status
from Security.deps import get_cur_user


def allow_roles(*roles):
    def checker(user=Depends(get_cur_user)):
        if user["role"] not in roles:
            raise HTTPException(
                status_code=403,
                detail="Permission denied"
            )
        return user

    return checker