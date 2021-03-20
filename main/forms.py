from django import forms

from main.models import ContactForm


class ContactFormForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ContactFormForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = ContactForm
        fields = ['email', 'project', 'question']

        widgets = {
            'email': forms.EmailInput(attrs={
                'placeholder': 'Введите ваш Email'
            })
        }