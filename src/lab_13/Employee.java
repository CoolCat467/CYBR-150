// Copyright (C) 2025  CoolCat467
//
// This program is free software: you can redistribute it and/or modify
// it under the terms of the GNU General Public License as published by
// the Free Software Foundation, either version 3 of the License, or
// (at your option) any later version.
//
// This program is distributed in the hope that it will be useful,
// but WITHOUT ANY WARRANTY; without even the implied warranty of
// MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
// GNU General Public License for more details.
//
// You should have received a copy of the GNU General Public License
// along with this program.  If not, see <https://www.gnu.org/licenses/>.

public class Employee extends Person {
    private double salary;

    public Employee(){
        super();
        this.setSalary(0.0);
    }

    public Employee(String first_name, String middle_name, String last_name, double salary){
        super(first_name, middle_name, last_name);
        this.setSalary(salary);
    }

    public boolean equalTo(Employee other){
        return (
            super.equalTo(other)
            && this.getSalary() == other.getSalary()
        );
    }

    public void setSalary(double salary){
        this.salary = salary;
    }
    public double getSalary(){
        return this.salary;
    }
    public String toString(){
        String previous = super.toString();
        previous = previous.substring(0, previous.length() - 1);
        return previous + ", salary=" + this.getSalary() + ")";
    }
}
