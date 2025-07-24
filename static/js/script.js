// document.addEventListener('DOMContentLoaded', function () {
//     const input = document.getElementById('searchInput');
//     const cards = document.querySelectorAll('.movie-card');

//     input.addEventListener('keyup', function () {
//         const filter = input.value.toLowerCase();

//         cards.forEach(function (card) {
//             const title = card.querySelector('.movie-title').textContent.toLowerCase();
//             if (title.includes(filter)) {
//                 card.style.display = 'block';
//             } else {
//                 card.style.display = 'none';
//             }
//         });
//     });
// });
 
// document.addEventListener('DOMContentLoaded', function () {
//     const movieid = document.getElementById('movie-id').dataset.movieid;
//     console.log(movieid);
// });

//  const ctx = document.getElementById('movieChart');
//   const movieid = document.getElementById('movie-id').dataset.movieid;
//   const api = `/movie_chart_data/${moviePk}`
//   fetch(api)
//   .then(res => res.json())
//   .then(data =>{
//     new Chart(ctx, {
//       type: 'line',
//       data: {
//         // labels: ['Red', 'Blue', 'Yellow', 'Green', 'Purple', 'Orange'],
//         labels: ['rottentomatoes','boxofficecollection'],
//         datasets: [{
//           label: '# of CGPA',
//           data: [data.rottentomatoes,data.boxofficecollection],
//           backgroundColor: 'rgba(54, 162, 235, 0.5)',
//           borderColor: 'rgba(54, 162, 235, 1)',
//           borderWidth: 1
//         }]
//       },
//       options: {
//         scales: {
//           y: {
//             beginAtZero: true
//           }
//         }
//       }
//     });
//   })


