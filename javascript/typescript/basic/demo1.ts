interface Person {
    firstName: string;
    lastName: string;
}

function greeter(person: Person){
    return "hello" + person.firstName + person.lastName
}

class Student {
    fullName: string;
    constructor(public firstName, public lastName) {
        this.fullName = firstName + lastName
    }
}

let user = new Student("jim", "stark");

document.body.innerHTML = greeter(user);
