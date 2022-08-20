// Store our API endpoint as queryUrl.
let queryUrl = "/get_data";

// Perform a GET request to the query URL/
d3.json(queryUrl).then(function (data) {

  console.log(data)
  
  $(document).ready(function () {
    $('#table').DataTable({
        data: data,
        columns: [
            { title: 'Year' },
            { title: 'Make' },
            { title: 'Model' },
            { title: 'Final Price' },
            { title: 'Mileage' },
            { title: 'Engine' },
            { title: 'Zipcode' }
  
        ],
    });
  });
});






