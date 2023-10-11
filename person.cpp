#include <cstdlib>
// Person class 

class Person{
	public:
		Person(int);
		int getAge();
		void setAge(int);
		double getDecades();
		int fib();
	private:
		int age;
		int fib_helpf(int);
	};
 
Person::Person(int a){
	age = a;
	}

int Person::fib(){
	return fib_helpf(getAge());
}

int Person::fib_helpf(int n){
	if(n<=1){return n;}
	return fib_helpf(n-1) + fib_helpf(n-2)
}

int Person::getAge(){
	return age;
	}
 
void Person::setAge(int a){
	age = a;
	}

double Person::getDecades(){
	return age/10.0;
}

extern "C"{
	Person* Person_new(int n) {return new Person(n);}
	int Person_get(Person* person) {return person->get();}
	void Person_set(Person* person, int n) {person->set(n);}
	void Person_delete(Person* person){
		if (person){
			delete person;
			person = nullptr;
			}
		}
	}