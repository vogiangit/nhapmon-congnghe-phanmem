//Chuyển dữ liệu từ json lên html
//Phần deadline
fetch(`data/ddata.json`)
    .then(function(response){
        return response.json();
    })
    .then(function(products) {
        let placeholder = document.querySelector("#dataload");
        let out = "";
        for (let product of products) {
            out += `
                <tr>
                    <td><a href="${product.ConferLink}">${product.Conference}</a></td>
                    <td>${product.Location}</td>
                    <td>${product.Deadline}</td>
                    <td>${product.Date}</td>
                    <td>${product.Notification}</td>
                    <td>${product.Subformat}</td>
                </tr>
            `;
        }
        placeholder.innerHTML = out;
    })

//Phần future
fetch(`data/fdata.json`)
    .then(function(response){
        return response.json();
    })
    .then(function(products) {
        let placeholder = document.querySelector("#fdataload");
        let out = "";
        for (let product of products) {
            out += `
                <tr>
                    <td><a href="${product.LinkName}">${product.Name}</td>
                    <td>${product.Location}</td>
                    <td>${product.Date}</td>
                    <td>${product.Notification}</td>
                    <td>${product.Final}</td>
                    <td>${product.Registration}</td>
                    <td>${product.Remark}</td>
                </tr>
            `;
        }
        placeholder.innerHTML = out;
    })

//Phần planning
fetch(`data/pdata.json`)
    .then(function(response){
        return response.json();
    })
    .then(function(products) {
        let placeholder = document.querySelector("#planningdata");
        let out = "";
        for (let product of products) {
            out += `
                <tr>
                    <td><a href="${product.hrefconf}">${product.Conference}</a></td>
                    <td>${product.year}</td>
                    <td>${product.location}</td>
                    <td>${product.startingdate}</td>
                    <td>${product.endingdate}</td>
                    <td>${product.remark}</td>
                </tr>
            `;
        }
        placeholder.innerHTML = out;
    })
//Phần Running
fetch(`data/rdata.json`)
    .then(function(response){
        return response.json();
    })
    .then(function(products) {
        let placeholder = document.querySelector("#datarun");
        let out = "";
        for (let product of products) {
            out += `
                <tr>
                    <td><a href=${product.hrefconf}>${product.Conference}</a></td>
                    <td>${product.Location}</td>
                    <td>${product.Date}</td>
                    <td>${product.Remark}</td>               
                </tr>
            `;
        }
        placeholder.innerHTML = out;
    })