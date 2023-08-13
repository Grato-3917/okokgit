fetch("SymptomsOutput.json")
.then(function(data){
    return data.json();
})
.then(function(SymptomsOutput){
    let placeholder = document.querySelector("td")
    let  out ="";
    for (let Symptom of SymptomsOutput){
        out += `
            <tr>
            <td>${Symptom["text"]}</td>
            <td>${Symptom["laytext"]}</td>
            <td>${Symptom["name"]}</td>
            <td>${Symptom["type"]}</td>
            <td>${Symptom["min"]}</td>
            <td>${Symptom["max"]}</td>
            <td>${Symptom["default"]}</td>
            <td>${Symptom["category"]}</td>
            <td>${Symptom["IsPatientProvided"]}</td>
            </tr>
            `;
    }
    
    placeholder.innerHTML = out;
    })
    