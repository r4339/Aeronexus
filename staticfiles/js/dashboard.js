/* ======================================================
   AERONEXUS
   Dashboard Javascript
====================================================== */

document.addEventListener("DOMContentLoaded", function () {

    console.log("AeroNexus Dashboard Loaded");

  

    animateCards();

    animateCounters();

    initCharts();

});







/*======================================================
    ANIMATED COUNTERS
======================================================*/

function animateCounters(){

    const counters=document.querySelectorAll(".counter");

    counters.forEach(counter=>{

        const target=parseInt(counter.innerText);

        let count=0;

        const speed=Math.ceil(target/60);

        counter.innerHTML="0";

        const update=()=>{

            count+=speed;

            if(count>=target){

                counter.innerHTML=target;

            }else{

                counter.innerHTML=count;

                requestAnimationFrame(update);

            }

        }

        update();

    });

}



/*======================================================
    CARDS
======================================================*/

function animateCards(){

    const cards=document.querySelectorAll(".kpi-card");

    cards.forEach(function(card,index){

        card.style.opacity=0;

        card.style.transform="translateY(30px)";

        setTimeout(function(){

            card.style.transition=".6s";

            card.style.opacity=1;

            card.style.transform="translateY(0px)";

        },index*120);

    });

}









/*======================================================
    CHARTS
======================================================*/

function initCharts(){

    const chart=document.getElementById("dashboardChart");

    if(!chart) return;

    new Chart(chart,{

        type:"bar",

        data:{

            labels:[

                "Utilisateurs",

                "Actifs",

                "Demandes",

                "Habilitations",

                "Audit",

                "Conformité"

            ],

            datasets:[{

                label:"Statistiques",

                data:[

                    usersCount,

                    assetsCount,

                    requestsCount,

                    permissionsCount,

                    auditCount,

                    complianceCount

                ],

                borderWidth:1,

                borderRadius:10

            }]

        },

        options:{

            responsive:true,

            maintainAspectRatio:false,

            plugins:{

                legend:{

                    display:false

                }

            },

            scales:{

                y:{

                    beginAtZero:true

                }

            }

        }

    });

}





/*======================================================
    DARK MODE (préparé)
======================================================*/

const dark=document.getElementById("darkMode");

if(dark){

    dark.addEventListener("click",function(){

        document.body.classList.toggle("dark");

    });

}


