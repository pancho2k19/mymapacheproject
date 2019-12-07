function confirmacion(id) {

 var caca = confirm("desea eliminar la pieza?")
 if (caca == true) {
   alert("La pieza ha sido eliminada con exito");
   window.location.href = "/eliminar/"+id+"/";

 }
}
