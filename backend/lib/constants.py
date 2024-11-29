from enum import Enum, IntEnum


class ErrorCodeEnum(IntEnum):
    # 服务器错误
    SERVER_ERROR = 10000502
    # 没有登陆
    UNAUTHORIZED = 10000401
    # 没有权限
    FORBIDDEN = 10000403
    # 不存在
    NOT_FOUND = 10000404
    # 已经存在
    ALREADY_EXISTS = 10000409
    # 参数错误
    VALIDATION_ERROR = 10000422
    # 提示错误
    USER_ERROR = 10000410


class STATUS(IntEnum):
    NORMAL = 0
    DELETE = -100


class UserErrorMsg:
    USER_NOT_FOUND = "用户不存在"
    USER_ALREADY_EXISTS = "用户已存在"
    USER_PASSWORD_ERROR = "密码错误"
    USER_NOT_ACTIVE = "用户未激活"
    USER_NOT_LOGIN = "用户未登录"
    USER_NOT_PERMISSION = "用户无权限"
    USER_NOT_FOUND_PERMISSION = "用户未找到权限"
    USER_NOT_FOUND_ROLE = "用户未找到角色"
    DATA_NOT_FOUND = "数据不存在"
    STATUS_NOT_DELETE = "当前状态不可删除"
    STATUS_NOT_EDIT = "当前状态不可编辑"
    PARAMS_ERROR = "缺少必要参数"
    USER_NOT_REGISTER = "用户未注册"
    ACCOUNT_PASSWORD_ERROR = "账号或密码不正确，请输入正确的账号密码"
    PHONE_ERROR = "手机号格式有误，请重新输入"
    SMS_CODE_ERROR = "短信验证码错误"
    TOKEN_NEED = "登录过期,请重新登录"
    USER_LOGINING = "该账号已在其他设备上登录,请重新登录"
    INVALID_TOKEN = "身份验证失败,请重新登录"
    UNKNOWN_ERROR = "未知错误"
    PASSWORD_ERROR_1 = "密码不一致"
    SMS_CODE_EXIT = "60秒内请勿重复发送"
    USER_LOGIN_NO = "账号异常，请联系管理员处理"
































































