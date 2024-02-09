from django import forms

class TodoListForm(forms.Form):
    text = forms.CharField(max_length=45,
        widget = forms.TextInput(
          attrs={'class':'forms_control', 'placeholder':'Enter todo eg shopping','aria_label':'Todo','aria_describeby':'add_btn'}))
