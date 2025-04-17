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

public class Employee extends User {
    private int employee_id;
    private String email;

    public Employee(){
        super();
        this.setEmployeeId(0);
        this.setEmail("<unset email>");
    }

    public Employee(String first_name, String middle_name, String last_name, int birthday, int employee_id, String email){
        super(first_name, middle_name, last_name, birthday);
        this.setEmployeeId(employee_id);
        this.setEmail(email);
    }

    public boolean equalTo(Employee other){
        return (
            super.equalTo(other)
            && this.getEmployeeId() == other.getEmployeeId()
            && this.getEmail().equals(other.getEmail())
        );
    }

    public void setEmployeeId(int employee_id){
        this.employee_id = employee_id;
    }
    public void setEmail(String email){
        this.email = email;
    }
    public int getEmployeeId(){
        return this.employee_id;
    }
    public String getEmail(){
        return this.email;
    }
    public String toString(){
        String previous = super.toString();
        previous = previous.substring(0, previous.length() - 1);
        return previous + ", employee_id=" + this.getEmployeeId() + ", email=" + this.getEmail() + ")";
    }
}
