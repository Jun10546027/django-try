from django import forms



class ContactForm(forms.Form):
    full_name = forms.CharField()
    email = forms.EmailField()
    content = forms.CharField(widget= forms.Textarea)


    #設計提醒訊息（invalid# arguments keyword arguments
    def clean_email(self,*args,**kwargs):

        #從ContactForm中用cleaned_data撈出字典，並用get找尋email
        email = self.cleaned_data.get('email')

        print(email)

        #如果email的結尾是.edu，就出現錯誤訊息
        if email.endswith('.edu'):
            raise forms.ValidationError("這不是有效的信箱")

        return email
    #-------------------------------------------
