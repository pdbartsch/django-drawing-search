from django import forms

class SearchForm(forms.Form):
    locnum = forms.IntegerField(label='Location Number', required=False)
    drawnum = forms.IntegerField(label='Drawing Number', required=False)
    projtitle = forms.CharField(label='Project Title', required=False, max_length=60)
    shttitle = forms.CharField(label='Sheet Title', required=False, max_length=60)
    shtnum = forms.CharField(label='Sheet Number', required=False, max_length=10)
    discp = forms.CharField(label='Discipline', required=False, max_length=25)
    drawdate = forms.IntegerField(label='Year', required=False)

# Discipline, DrawingDate, DrawingNumber, DrawingVersion, LocationNumber, NewName, Notes, OldName, PhysicalLocation, ProjectNumber, ProjectTitle, SheetNumber, SheetTitle, id


# <form action="/search/" method="GET">

#     <div class="form-group">
#         <label for="locationNumber">Location Number:</label>
#         <input type="number" name="locnum" class="form-control" id="locationNumber" aria-describedby="locationNumberHelp" placeholder="Location Number" value="{{ request.GET.locnum }}">
#         <small id="locationNumberHelp" class="form-text text-muted">Normally this is the building number</small>
#     </div>
#     <div class="form-group">
#         <label for="drawingNumber">Drawing Number:</label>
#         <input type="number" name="drawnum" class="form-control" id="drawingNumber" aria-describedby="drawingNumberHelp" placeholder="Drawing Number" value="{{ request.GET.drawnum }}">
#         <small id="drawingNumberHelp" class="form-text text-muted">Original construction is 101 and they go up sequentially from there.</small>
#     </div>
#     <div class="form-group">
#             <label for="projectTitle">Project Title:</label>
#             <input type="text" name="projtitle" class="form-control" id="projectTitle" aria-describedby="projectTitleHelp" placeholder="Project Title" value="{{ request.GET.projtitle }}">
#     </div>
#     <div class="form-group">
#             <label for="sheetTitle">Sheet Title:</label>
#             <input type="text" name="shttitle" class="form-control" id="sheetTitle" aria-describedby="sheetTitleHelp" placeholder="Sheet Title" value="{{ request.GET.shttitle }}">
#     </div>
#     <div class="form-group">
#             <label for="sheetNumber">Sheet Number:</label>
#             <input type="text" name="shtnum" class="form-control" id="sheetNumber" aria-describedby="sheetNumberHelp" placeholder="Sheet Number" value="{{ request.GET.shtnum }}">
#     </div>
#     <!-- improvement: discp is the only field that isn't 'sticky' -->
#     <div class="form-group">
#         <label for="designDesignation">Design Designation</label>
#         <select class="form-control" name="discp" id="designDesignation">
#             <option value="">ANY</option>
#             <option>ARCHITECTURAL</option>
#             <option>AUDIO VISUAL</option>
#             <option>CIVIL</option>
#             <option>ELECTRICAL</option>
#             <option>FIRE ALARM</option>
#             <option>GENERAL NOTES</option>
#             <option>LANDSCAPE</option>
#             <option>LIFE SAFETY</option>
#             <option>MECHANICAL</option>
#             <option>PLUMBING</option>
#             <option>SHOP DRAWINGS</option>
#             <option>SPECIFICATIONS</option>
#             <option>STRUCTURAL</option>
#             <option>TELECOMM</option>
#             <option>TITLE INDEX</option>
#             <option>TRAFFIC</option>
#             <option>O&M Manual</option>
#         </select>
#     </div>
#     <div class="form-group">
#             <label for="drawingDate">Year Since (yyyy):</label>
#             <input type="number" name="drawdate" class="form-control" id="drawingDate" aria-describedby="drawingDateHelp" placeholder="YYYY" value="{{ request.GET.drawdate }}">
#     </div>
#     <button type="submit" class="btn btn-primary">Submit</button>
# </form>
