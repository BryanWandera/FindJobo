document.addEventListener("DOMContentLoaded", (event)=>{

document.getElementById("cities-dropdown").addEventListener("change", (event)=>{


    var selectedCity = document.getElementById("cities-dropdown").value
    location.href = `/${selectedCity}/`

    document.getElementById("selected-city").setAttribute("value", `${selectedCity}`)
    document.getElementById("selected-city").innerHTML = selectedCity

    


})

// var categoryTabs = document.getElementsByClassName("category-container")
// console.log(categoryTabs)

// for (var i = 0; i < categoryTabs.length; i++) {
//     /// add event listener
//     categoryTabs[i].addEventListener("click", (event)=>{
//         // when clicked, deactivate all tabs
//         for (var j = 0; j< categoryTabs.length; j++){
//             categoryTabs[j].setAttribute("color", "black")
//         }

//         // then select this tab
//         console.log(i)
//         categoryTabs[i].setAttribute("color", "green")
//     })
    
//  }



    
})

