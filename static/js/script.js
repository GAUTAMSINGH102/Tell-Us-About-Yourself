const firstname = document.getElementById("1"),
study = document.getElementById("2"),
degree = document.getElementById("3"),
company = document.getElementById("4"),
position = document.getElementById("5"),
responsibilities = document.getElementById("6"),
achievements = document.getElementById("7");

const parseLinkedIn = document.getElementById("parseLinkedInButton");

const generateDocument = document.getElementById("generateDocumentId");
// referralResponseArea = document.getElementById("referralResponseArea")

parseLinkedIn.onclick = function () {
        parse()
};

function parse() {
        linkedInLink = document.getElementById("parseLinkedInInput").value
        console.log("before link")
        console.log(linkedInLink)

        let xhr = new XMLHttpRequest();

        console.log('inside parse')
        xhr.open("POST", "/dev/parse", true);
        //Send the proper header information along with the request
        xhr.setRequestHeader("Content-Type", "application/json");

        xhr.onload = function () {
                console.log('inside parseLoad')
                if (this.status == 200) {
                        console.log(this.responseText)
                        profileInfo = JSON.parse(this.responseText)

                        firstnameValue = firstname.value = profileInfo['first_name']
                        studyValue = study.value = profileInfo['study']['schoolName']
                        degreeValue = degree.value = profileInfo['study']['degreeName']
                        companyValue = company.value = profileInfo['company']['companyName']
                        positionValue = position.value = profileInfo['position']
                        resValue = responsibilities.value = profileInfo['responsibilities']
                        achieveValue = achievements.value = profileInfo['achievements']

                        console.log(firstnameValue)

                        // generateDocumentFunc(firstnameValue, studyValue, degreeValue, companyValue, positionValue, resValue, achieveValue)

                        document.getElementById("generateDocumentId").onclick = function () {
                                generateDocumentFunc(firstnameValue, studyValue, degreeValue, companyValue, positionValue, resValue, achieveValue)
                        };
                }
                else {
                        console.log("inside parse else")
                }
        }
        params = { "link": linkedInLink }
        xhr.send(JSON.stringify(params));
}

function generateDocumentFunc(fname, study, degree, company, position, res, achieve) {
        const prompt =
                "Person name: " +
                fname +
                "," +
                "Place of education: " +
                study +
                "," +
                "Education degree: " +
                degree +
                "," +
                "Place of work: " +
                company +
                "," +
                "Position:  " +
                position +
                "," +
                "Responsibilities: " +
                res +
                "," +
                "Achievements: " +
                achieve;

                console.log(prompt);


        let xhr = new XMLHttpRequest();

        console.log('inside cohere')
        xhr.open("POST", "/dev/cohere", true);
        //Send the proper header information along with the request
        xhr.setRequestHeader("Content-Type", "application/json");

        xhr.onload = function () {
                console.log('inside cohereLoad')
                if (this.status == 200) {
                        console.log(this.responseText)
                        referralResponse = this.responseText

                        document.getElementById("referralResponseTextArea").value = referralResponse
                }
                else {
                        console.log("inside cohere else")
                }
        }
        params = { "person_info": prompt }
        xhr.send(JSON.stringify(params));
}