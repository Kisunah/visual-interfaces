


// d3.csv('data/worldcities.csv')
//   .then(data => {
//     data.forEach(d => {
//       d.latitude = +d.lat; //make sure these are not strings
//       d.longitude = +d.lng; //make sure these are not strings
//     });

//     console.log(data);//ok, got my data!

//     // Initialize chart and then show it
//     leafletMap = new LeafletMap({ parentElement: '#my-map' }, data);


//   })
//   .catch(error => console.error(error));

d3.csv('data/data-sample2.csv')
  .then(data => {
    data.forEach(d => {
      if (d.decimalLatitude == 'null') d.decimalLatitude = 9999999;
      if (d.decimalLongitude == 'null') d.decimalLongitude = 999999;
      d.latitude = +d.decimalLatitude; //make sure these are not strings
      d.longitude = +d.decimalLongitude; //make sure these are not strings
    });

    console.log(data);//ok, got my data!

    // Initialize chart and then show it
    leafletMap = new LeafletMap({ parentElement: '#my-map' }, data);


  })
  .catch(error => console.error(error));
