/*Author: Scott Normore

Progam for QAP 4. It uses the information in the customer object, and appends that information
to the body of the html file.

*/

// Function that I made to display the date in a nicer format (instead of a really long explicit string)
formatDate = function(date) {
    year = date.getFullYear()
    month = date.getMonth()
    day = date.getDate()
    return year+"-"+month+"-"+day
}

//the customer object
const customer = {
    //Attribures of the customer
    custName : "Bill Nye",
    custBDay : new Date("1955-11-27"),
    custGender : "Male",
    custRoomPref : [102,104,113,154],
    custPayment : "Credit Card",
    custMailAdr : {
        streetAddress : '21 "Did you know?"lane',
        postalCode : "A9A 9A9"
    },
    custPNumber : "999-999-9999",
    checkInfo : {
        checkInTime : new Date("2023-03-17"),
        checkOutTime : new Date("2023-03-20")
    },
    //functions and calculations derived from the attributes
    calculateDuration : function() {
        difference = (this.checkInfo.checkOutTime - this.checkInfo.checkInTime)
        differenceInDays = difference / (1000 * 60 * 60 * 24)
        return differenceInDays
    },
    calculateAge : function(){
        difference = Date.now() - this.custBDay
        //I floor the difference, since some one who is 67.86 years old is still considered 67
        //I also assume 365 days in a year
        differenceInYears = Math.floor(difference / (1000 * 60 * 60 * 24 * 365))
        return differenceInYears
    }
}


// Using a template literal, I append the customer information as one big string to the body of the html file
document.body.innerHTML = `<p>
                                Customer Name: ${customer.custName} <br>
                                Customer Birthday: ${formatDate(customer.custBDay)} <br>
                                Age of Customer: ${customer.calculateAge()} Gender: ${customer.custGender} <br>
                                Prefered Rooms: ${customer.custRoomPref} <br>
                                Customer Payment Method: ${customer.custPayment} <br>
                                Customer Street Adress: ${customer.custMailAdr.streetAddress} <br>
                                Customer Postal Code: ${customer.custMailAdr.postalCode} <br>
                                Customer Phone Number: ${customer.custPNumber} <br>
                                Booking Start Date: ${formatDate(customer.checkInfo.checkInTime)} <br>
                                Booking End Date: ${formatDate(customer.checkInfo.checkOutTime)} <br>
                                Duration of Stay (in days): ${customer.calculateDuration()}
                            </p>
                            `