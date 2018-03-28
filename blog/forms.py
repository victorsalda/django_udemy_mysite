"""" Forms are objects to help accept input from site visitors, and then process and respond to the input.

The Hypertext Transfer Protocol (HTTP) is designed to enable communications between clients and servers.
HTTP works as a request-response protocol between a client and server.

GET and POST are the only HTTP methods to use when dealing with forms.
A web browser may be the client, and an application on a computer that hosts a web site may be the server.

GET and POST are the two commonly used methods for a request-response between a client and server are.

GET - Requests data from a specified resource.
POST - Submits data to be processed to a specified resource.

In computing, POST is a request method supported by HTTP used by the World Wide Web. By design, the POST
request method requests that a web server accepts the data enclosed in the body of the request message,
most likely for storing it.It is often used when uploading a file or when submitting a completed web form.

In contrast, the HTTP GET request method retrieves information from the server.
As part of a GET request, some data can be passed within the URL's query string, specifying (for example)
search terms, date ranges, or other information that defines the query.

In the context of a Web application, ‘form’ might refer to that HTML <form>, or to the Django Form
that produces it, or to the structured data returned when it is submitted, or to the
end-to-end working collection of these parts. """


from django import forms
from .models import Comment

class EmailPostForm(forms.Form): # for
    name = forms.CharField(max_length=25) # form’s fields are themselves classes; they manage form data and perform validation when a form is submitted
    email = forms.EmailField()
    to = forms.EmailField()
    comments = forms.CharField(required=False, widget=forms.Textarea) # this field is optional.

class CommentForm(forms.ModelForm):  # we are creating a form from a model. So we need to indicate which model.
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body') # fields of the forms.

class SearchForm (forms.Form):
    query = forms.CharField()
