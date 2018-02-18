var socket = io();

var connection = io.connect("localhost:8080");

connection.on("connect", function(){
  console.log("Connected to server");
});

function onSubmit() {
  var phone_number = document.getElementById('submit_box').value;
  var carrier = document.getElementById("carrier_menu").value;
  phone_number = phone_number.replace(/\D/g,'');
  if (phone_number.length == 10) {
      console.log(phone_number + " " + carrier);
      var data = {
        phone_number: phone_number,
        carrier: carrier
      };

      connection.emit("data", data);
  }
}

