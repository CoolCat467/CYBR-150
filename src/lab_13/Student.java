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

public class Student extends Person {
    private int number;

    public Student(){
        super();
        this.setNumber(0);
    }

    public Student(String first_name, String middle_name, String last_name, int number){
        super(first_name, middle_name, last_name);
        this.setNumber(number);
    }

    public boolean equalTo(Student other){
        return (
            super.equalTo(other)
            && this.getNumber() == other.getNumber()
        );
    }

    public void setNumber(int number){
        this.number = number;
    }
    public int getNumber(){
        return this.number;
    }
    public String toString(){
        String previous = super.toString();
        previous = previous.substring(0, previous.length() - 1);
        return previous + ", number=" + this.getNumber() + ")";
    }
}
