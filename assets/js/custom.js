$("#searchForm").hide()
$(document).ready(function(){
  $("#toggleSearch").click(function(){
    $("#searchForm").toggle("slow");
  });
});