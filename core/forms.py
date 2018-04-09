from django import forms


class ContactForm(forms.Form):

    #required default True
    #Cria os formulários
    #form = ContactForm()
    #form.as_p(), form.is_valid(), form.errors
    name = forms.CharField(label='Nome')
    email = forms.EmailField(label='E-mail')
    message = forms.CharField(label='Mensagem', widget=forms.Textarea)

