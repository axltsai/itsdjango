#!/usr/bin/env python
#coding:utf8
#Created by axltsai on 2016/02/29 09:14

from django import forms


class CommentForm(forms.Form):
    visitor = forms.CharField(max_length = 20, label = '您的大名')
    email = forms.EmailField(max_length = 20, required = False, label = '電子信箱')
    content = forms.CharField(max_length = 200, widget = forms.Textarea(), label = '評論內容')

    def clean_content(self):
        content = self.cleaned_data['content']
        if len(content) < 5:
            raise forms.ValidationError('字數不足五個字')
        return content





