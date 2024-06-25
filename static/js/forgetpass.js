const form = document.querySelector("form")

form.addEventListener("submit",(e)=>{
    e.preventDefault()

    const email = form.email.value
    const password = form.password.value

    const authenticated = authentication(username,password)

    if(authenticated){
        alert("correct")
    }else{
        alert("wrong")
    }
})



function authentication(username,password){
    if(email === "abc110145@gmail.com" && password === "password"){
        return true
    }else{
        return false
    }
}