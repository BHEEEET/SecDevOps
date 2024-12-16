print("Hello world!")
print("Dev")

password = "12345"  # Dit moet gedetecteerd worden.


eval("print('Dit is onveilig!')")

eval("os.system('echo Hacked!')")  # Onveilig gebruik van eval.

user_input = "print('Kwetsbare eval')"
eval(user_input)  # Dit moet gedetecteerd worden door CodeQL.
 
api_key = "sk_test_51H3UjbvK4jLopL3yDe0g7G0asf"
password = "SuperSecret123"


test_server = 'http://user:password@192.168.0.1:3128'

aws_secret_key = "AKIAIOSFODNN7EXAMPLE"

aws_secret = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"

aws_session_token = "AQoEXAMPLEH4aoAH0gNCAPyJxz4BlCFFxWNE1OPTgk5TthT+FvwqnKwRcOIfrRh3c/LTo6UDdyJwOOvEVPvLXCrrrUtdnniCEXAMPLE/IvU1dYUg2RVAJBanLiHb4IgRmpRV3zrkuWJOgQs8IZZaIv2BXIa2R4OlgkBN9bkUDNCJiBeb/AXlzBBko7b15fjrBs2+cTQtpZ3CYWFXG8C5zqx37wnOE49mRl/+OtkIKGO7fAE"