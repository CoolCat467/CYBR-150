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

public class Person {
    private String first_name;
    private String middle_name;
    private String last_name;

    public Person(){
        this("<unset first name>", "<unset middle name>", "<unset last name>");
    }

    public Person(String first_name, String middle_name, String last_name){
        this.setFirstName(first_name);
        this.setMiddleName(middle_name);
        this.setLastName(last_name);
    }

    public boolean equalTo(Person other){
        return (
            this.getFirstName().equals(other.getFirstName())
            && this.getMiddleName().equals(other.getMiddleName())
            && this.getLastName().equals(other.getLastName())
        );
    }

    public void setFirstName(String first_name){
        this.first_name = first_name;
    }
    public void setMiddleName(String middle_name){
        this.middle_name = middle_name;
    }
    public void setLastName(String last_name){
        this.last_name = last_name;
    }
    public String getFirstName(){
        return this.first_name;
    }
    public String getMiddleName(){
        return this.middle_name;
    }
    public String getLastName(){
        return this.last_name;
    }
    public String toString(){
        return super.toString() + "(first_name=" + this.getFirstName() + ", middle_name=" + this.getMiddleName() + ", last_name=" + this.getLastName() + ")";
    }
}
