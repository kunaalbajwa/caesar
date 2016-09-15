import webapp2
from caesar import *
from helpers import *
#put escape function
page_header = """
<!DOCTYPE html>

<html>
    <head>
    <title>SignUp</title>
</head>
<body>

 """
page_footer= """
</body>
</html>
 """


class Index(webapp2.RequestHandler):
    def get(self):

        input_form = """
<p> Enter a message. It will encrypt to a 13
rotation unless specified.</p>
    <form action = "/input" method ="post">
        <label>
            Message:
            <input type = "text" name ="message"/>
        </label>

        <label>
            Rotation Amount:
            <input type = "number" name = "rot"/>
        </label>
        <input type ="submit" value ="Rotate"/>
        </form>

        """
        respond = page_header + input_form + page_footer
        self.response.write(respond)

class rotate(webapp2.RequestHandler):
    def post(self):
        wds= ''
        rot = 13
        empty = ''
        if (self.request.get("message") == ''):
            empty= "You forgot to type a message! Please do that so we can encrypt. Wouldnt that be fun?"
            respond = page_header + empty+ page_footer
        elif (self.request.get("rot") != ''):
            rot = int(self.request.get("rot"))
        wds = str(self.request.get("message"))
        new_wds= encrypt(wds, rot)
        display= "<p>The previous message: </p>" +wds + "<p>The new message:</p>" + new_wds
        respond = page_header + display + page_footer
        self.response.write(respond)
app= webapp2.WSGIApplication ([
('/', Index),
('/input', rotate)
 ], debug=True)
