function clearImg(){
    var img = document.getElementById("img1");
    img.src="static/images/no-image.svg";
}

function onSubmit() {
    var myVar = document.getElementById("myVar").value;
    alert(myVar)
}

$('#inputGroupFile04').on('change', function() { 
    let fileName = $(this).val().split('\\').pop();
    console.log(fileName)
    $(this).next('.custom-file-label').addClass("selected").html(fileName); 
 });