function Expiry()
{
// Get the Expiry Date
var ED = util.scand("dd/mm/yyyy","14/06/2018"); // Expiration date is 14th June 2018. Change this date to suit your needs
 
// Get Today's Date
var TD = new Date();
 
// Validate and take measures!
var diff = (((((ED.valueOf() - TD.valueOf()) / 1000) / 60) / 60) / 24); // Days difference
if (diff < 1) {
// Now the prompt...
app.alert("Sorry this document has now expired. You cannot use this specific document any further.\n___________________________________________\n\nSo sorry.", 0, 0);
 
// Dont Save and Close Document
DontSave = true
this.closeDoc(DontSave)
};
}
 
// execute check expiration code
Expiry();