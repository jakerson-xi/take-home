var minDate, maxDate;

// Custom filtering function which will search data in column four between two values
$.fn.dataTable.ext.search.push(function (settings, data, dataIndex) {
  var min = minDate.val();
  var max = maxDate.val();
  var date = moment(data[1], "MMM DD, YYYY");
  console.log("min:", min);
  console.log("max:", max);
  console.log("date:", date);
  if (
    (min === null && max === null) ||
    (min === null && date <= max) ||
    (min <= date && max === null) ||
    (min <= date && date <= max)
  ) {
    return true;
  }
  return false;
});

$(document).ready(function () {
  minDate = new DateTime($("#min"), {
    format: "MMMM Do YYYY",
  });
  maxDate = new DateTime($("#max"), {
    format: "MMMM Do YYYY",
  });
  // Refilter the table

  var table = $("#purchase_table").DataTable({
    responsive: true,
    order: [[1, "asc"]],
    buttons: [
      {
        extend: "excel",
        className: "btn btn-warning mt-3 me-1 border border-secondary",
        text: '<i class="bi bi-download"></i> Download as Excel',
        filename: "purchase_table",
        title: "purchase_table",
        exportOptions: {
          columns: [0, 1, 2, 3, 4, 5],
        },
      },
      {
        extend: "pdf",
        className: "btn btn-warning mt-3 border border-secondary",
        text: '<i class="bi bi-download"></i> Download as PDF',
        filename: "purchase_table",
        title: "purchase_table",
        exportOptions: {
          columns: [0, 1, 2, 3, 4, 5, 6],
        },
      },
    ],
  });

  $("#min, #max").on("change", function () {
    table.draw();
  });

  table
    .buttons()
    .container()
    .appendTo("#purchase_table_wrapper .col-md-6:eq(0)");
});
