$(function () {
	$(".editable").dblclick(function () {  
		var OriginalContent = $(this).text(); 
		$(this).addClass("cellEditing"); 
		$(this).html("<input type='text' class='form-control' value='" + OriginalContent + "' />"); 
		$(this).children().first().focus();
		
		$(this).children().first().keypress(function (e) { 
			if (e.which == 13) 
			{ 
				var newContent = $(this).val(); 
				$(this).parent().text(newContent); 
				$(this).parent().removeClass("cellEditing"); }
			});
		
		$(this).children().first().blur(function(){
			var newContent = $(this).val(); 
			$(this).parent().text(newContent); 
			$(this).parent().removeClass("cellEditing");
		}); 
	}); 
});


$(function () { 
	$(".changetoSelectBox").dblclick(function () { 
		$(this).html("<select class='form-control'><option value='FD'>FD</option><option value='SAVING'>SAVING</option><option value='LIC'>LIC</option></select>");
	});
	
});

$(function () { 
	$(".dateEditable").dblclick(function () { 
		var OriginalContent = $(this).text(); 
		var id = $(this).attr("id")+"_";
		$(this).html("<input id ='"+ id  +"' class='form-control' value='" + OriginalContent + "' />");
		
		$("input#"+id).datepicker({
		      changeMonth: true,
		      changeYear: true,
		      yearRange: "1990:2050",
		      dateFormat: "yy-mm-dd",
		      onSelect: function(dateText, inst) {
		    	  	var newContent = $(this).val(); 
					$(this).parent().text(newContent);
		    	    }
		    	  
		    });
	});
	
	
});



$(function(){
    $("[id^='delete']").click(function() {
        var policyNumber = $(this).closest("tr").find('td:eq(2)').text();
        var flag = confirm("Do you really want to delete policy/investment with " +policyNumber+ " ?");
        
        if(flag){$.ajax({
            type: "POST",
            url: "policy/delete/",
            data: { policyNumber:policyNumber},
            success: function(response){
            	window.location.reload();
            }
        });
    }
    return false;
   });
});

$(function(){
    $("[id^='update']").click(function(){
        	var name = $(this).closest("tr").find('td:eq(0)').text();
        	var financeType =$(this).closest("tr").find('td:eq(1)').find(":selected").text();
        		if(financeType==""){
        			financeType =$(this).closest("tr").find('td:eq(1)').text();
        		}
        	var policyNumber = $(this).closest("tr").find('td:eq(2)').text();
        	var amount = $(this).closest("tr").find('td:eq(3)').text();
        	var issueDate = $(this).closest("tr").find('td:eq(4)').text();
        	var maturityDate = $(this).closest("tr").find('td:eq(5)').text();
        	var remarks = $(this).closest("tr").find('td:eq(6)').text();
        $.ajax({
            type: "POST",
            url: "policy/update/",
            data: {name:name,financeType:financeType,policyNumber:policyNumber,maturityDate:maturityDate,issueDate:issueDate, amount: amount, remarks:remarks},
            success: function(response){
                alert(response.success);
                window.location.reload();
            }
        });
        return false;
    });
});

// for date picker
$(function() {
    $( ".datepicker" ).datepicker({
      changeMonth: true,
      changeYear: true,
      yearRange: "1990:2050"
    });
  });

// pagination
$(document).ready(function() {
    $('#data').after('<div id="nav"></div>');
    
    var selected = document.getElementById('entries');
    var rowsShown = selected.options[selected.selectedIndex].value;
    
    var rowsTotal = $('#data tbody tr').length;
    var numPages = rowsTotal/rowsShown;
    for(i = 0;i < numPages;i++) {
        var pageNum = i + 1;
        $('#nav').append('<a href="#" rel="'+i+'">'+pageNum+'</a> ');
    }
    $('#data tbody tr').hide();
    $('#data tbody tr').slice(0, rowsShown).show();
    $('#nav a:first').addClass('active');
    $('#nav a').bind('click', function(){

        $('#nav a').removeClass('active');
        $(this).addClass('active');
        var currPage = $(this).attr('rel');
        var startItem = currPage * rowsShown;
        var endItem = startItem + rowsShown;
        $('#data tbody tr').css('opacity','0.0').hide().slice(startItem, endItem).
                css('display','table-row').animate({opacity:1}, 300);
    });
});

// for sorting
$(document).ready(function() 
	    { 
	        $("#data").tablesorter(); 
	    } 
	); 
// searching

$(document).ready(function()
		{
			$('#searchTerm').keyup(function()
			{
				doSearch($(this).val());
			});
		});

function doSearch(searchText) {
    var targetTable = document.getElementById('data');
    var targetTableColCount;
            
    //Loop through table rows
    for (var rowIndex = 0; rowIndex < targetTable.rows.length; rowIndex++) {
        var rowData = '';

        //Get column count from header row
        if (rowIndex == 0) {
           targetTableColCount = targetTable.rows.item(rowIndex).cells.length;
           continue; //do not execute further code for header row.
        }
                
        //Process data rows. (rowIndex >= 1)
        for (var colIndex = 0; colIndex < targetTableColCount; colIndex++) {
            rowData += targetTable.rows.item(rowIndex).cells.item(colIndex).textContent;
        }

        //If search term is not found in row data
        //then hide the row, else show
        if (rowData.indexOf(searchText) == -1)
            targetTable.rows.item(rowIndex).style.display = 'none';
        else
            targetTable.rows.item(rowIndex).style.display = 'table-row';
    }
}

// closing a panel
function closePanel() {
    document.getElementById("mainPanel").style.display = "none";
    
}

function closeAddButton() {
    document.getElementById("add").style.display = "none";
    
}
