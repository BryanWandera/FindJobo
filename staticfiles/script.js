document.addEventListener("DOMContentLoaded", (event)=>{

    //filter by city functionality
    document.getElementById("cities-dropdown").addEventListener("change", (event)=>{


        var selectedCity = document.getElementById("cities-dropdown").value
        location.href = `/${selectedCity}/`

        document.getElementById("selected-city").setAttribute("value", `${selectedCity}`)
        document.getElementById("selected-city").innerHTML = selectedCity

    
})
    //filter by category functionality
    document.getElementById("categories-dropdown").addEventListener("change", (event)=>{

        var selectedCity = document.getElementById("cities-dropdown").value
        var selectedCategory = document.getElementById("categories-dropdown").value
        location.href = `/${selectedCity}/${selectedCategory}`

        document.getElementById("selected-category").setAttribute("value", `${selectedCategory}`)
        document.getElementById("selected-category").innerHTML = selectedCategory

    


})


    
})

