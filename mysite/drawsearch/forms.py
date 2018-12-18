from django import forms

class SearchForm(forms.Form):
    locnum = forms.IntegerField(label='Location Number', required=False)
    drawnum = forms.IntegerField(label='Drawing Number', required=False)
    projtitle = forms.CharField(label='Project Title', required=False, max_length=60)
    shttitle = forms.CharField(label='Sheet Title', required=False, max_length=60)
    shtnum = forms.CharField(label='Sheet Number', required=False, max_length=10)
    # dropdown options for drawing discipline
    OPTIONS = (
    # by setting the default choice of 'Any' to None it is excluded from our filter. See views.result if statement 
    (None,'ANY'),
    ('ARCHITECTURAL','ARCHITECTURAL'),
    ('AUDIO VISUAL','AUDIO VISUAL'),
    ('CIVIL','CIVIL'),
    ('ELECTRICAL','ELECTRICAL'),
    ('FIRE ALARM','FIRE ALARM'),
    ('GENERAL NOTES','GENERAL NOTES'),
    ('LANDSCAPE','LANDSCAPE'),
    ('LIFE SAFETY','LIFE SAFETY'),
    ('MECHANICAL','MECHANICAL'),
    ('PLUMBING','PLUMBING'),
    ('SHOP DRAWINGS','SHOP DRAWINGS'),
    ('SPECIFICATIONS','SPECIFICATIONS'),
    ('STRUCTURAL','STRUCTURAL'),
    ('TELECOMM','TELECOMM'),
    ('TITLE INDEX','TITLE INDEX'),
    ('TRAFFIC','TRAFFIC'),
    ('O&M Manual','O&M Manual'),
    )
    discp = forms.CharField(label='Discipline', widget=forms.Select(choices=OPTIONS), required=False)
    drawdate = forms.IntegerField(label='Year', required=False)
