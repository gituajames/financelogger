
setTimeout(function () {

	console.log({{date_labels | safe }})

	// chart 1
	var ctx1 = document.getElementById('chart1').getContext('2d');
	var myChart1 = new Chart(ctx1, {
		type: 'line',
		data: {
			// labels: ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct"],
			labels: {{ date_labels | safe }}
			datasets: [{
				label: 'Daily sum for 30 days',
				// data: [3, 3, 8, 5, 7, 4, 6, 4, 6, 3],
				data: {{ date_sums | safe }}
				backgroundColor: '#14abef',
				borderColor: "transparent",
				pointRadius :"0",
				borderWidth: 3
			}, ]
		},
		options: {
			maintainAspectRatio: false,
			legend: {
				display: false,
				labels: {
					fontColor: '#585757',
					boxWidth:40
				}
			},
			tooltips: {
				displayColors:false
			},
			scales: {
				xAxes: [{
					ticks: {
						beginAtZero:true,
						fontColor: '#585757'
					},
					gridLines: {
						display: true ,
						color: "rgba(0, 0, 0, .05)"
					},
				}],
				yAxes: [{
					ticks: {
						beginAtZero:true,
						fontColor: '#585757'
					},
					gridLines: {
						display: true ,
						color: "rgba(0, 0, 0, .05)"
					},
				}]
			}

		}
	});


	// chart 2
	var ctx2 = document.getElementById("chart2").getContext('2d');
	var myChart2 = new Chart(ctx2, {
		type: 'doughnut',
		data: {
			labels: ["Direct", "Affiliate", "E-mail", "Other"],
			datasets: [{
				backgroundColor: [
					"#14abef",
					"#02ba5a",
					"#d13adf",
					"#fba540"
				],
				data: [5856, 2602, 1802, 1105],
				borderWidth: [0, 0, 0, 0]
			}]
		},
		options: {
			maintainAspectRatio: false,
			legend: {
				position :"bottom",
				display: false,
				labels: {
					fontColor: '#ddd',
					boxWidth:15
				}
			}
			,
			tooltips: {
				displayColors:false
			}
		}
	});

}, 1000)
