import webapp2
from caesar import *
from helpers import *
#put escape function
page_header = """
<!DOCTYPE html>

<html>
    <head>
    <title>Caesar</title>
</head>
<body>

 """
page_footer= """
</body>
</html>
 """
input_form = """
<p> Enter a message. It will encrypt to a 13
rotation unless specified.</p>

<label>
    Rotation Amount:
    <input type = "number" name = "rot"/>
</label>


<form action="/rotate" method="post">
<input type ="submit" value="Rotate"/>
<label>
<p>
    <textarea name="message" rows="10" cols="60">{message}</textarea></p>
</label>

</form>

"""
#text substitution
class Index(webapp2.RequestHandler):
    def get(self):

        respond = page_header + input_form.format(message="") + page_footer
        self.response.write(respond)



class rotate(webapp2.RequestHandler):
    #change like the example and have it change like in the box
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
        respond = page_header + input_form.format(message=new_wds) + page_footer
        self.response.write(respond)
app= webapp2.WSGIApplication ([
('/', Index),
('/rotate', rotate)
 ], debug=True)
