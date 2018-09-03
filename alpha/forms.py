#! _*_ coding:utf8 _*_

from django import forms
from django.forms import ModelForm
import assets.models


class ServersModuleForm(ModelForm):
    class Meta:
        # 使用模型Servers中的所有字段
        model = assets.models.Servers
        fields = '__all__'

    # 自定义ExpirationDate样式,覆盖掉之前的,新加自定义日历样式
    ExpirationDate = forms.DateField(
        widget=forms.DateTimeInput(
            attrs={'type': 'date'}
        ),
        label='到期时间'
    )


class ApplicationsModuleForm(ModelForm):
    class Meta:
        model = assets.models.Applications
        fields = '__all__'

        widgets = {
            'Name': forms.Select(
                choices=(
                    ('Nginx', 'Nginx'),
                    ('Tomcat', 'Tomcat'),
                    ('MySQL', 'MySQL'),
                    ('Redis', 'Redis'),
                    ('Sentinel', 'Sentinel'),
                    ('Logstash', 'Logstash'),
                    ('Kibana', 'Kibana'),
                    ('PHP', 'PHP'),
                    ('MongoDB', 'MongoDB'),
                    ('Dubbo', 'Dubbo'),
                    ('Zabbix', 'Zabbix'),
                    ('Jenkins', 'Jenkins'),
                    ('Confluence', 'Confluence'),
                    ('Gitlab', 'Gitlab'),
                    ('FastDFS', 'FastDFS'),
                    ('Zentao', 'Zentao'),
                    ('Nexus', 'Nexus'),
                    ('Keepalived', 'Keepalived'),
                    ('Haproxy', 'Haproxy'),
                )
            )
        }
