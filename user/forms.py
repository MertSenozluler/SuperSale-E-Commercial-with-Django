from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name','last_name','username', 'email', 'password1', 'password2']

    def  __init__(self,*args,**kwargs):
        super(UserForm,self).__init__(*args,**kwargs)
        for name,field in self.fields.items():
            field.widget.attrs.update({'class' : 'form-control'})
        # register da bütün heryere form-control sınıfını verdi
            field.help_text = ''
