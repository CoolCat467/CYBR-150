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

public class Animal {
    private String type;
    private int legs;
    private int size;
    private String name;

    public Animal(){
        this("<unset type>", 0, 0, "<unset name>");
    }

    public Animal(String type, int legs, int size, String name){
        this.setType(type);
        this.setLegs(legs);
        this.setSize(size);
        this.setName(name);
    }

    public boolean equalTo(Animal other){
        return (
            this.getType().equals(other.getType())
            && this.getLegs() == other.getLegs()
            && this.getSize() == other.getSize()
            && this.getName().equals(other.getName())
        );
    }

    public int compareTo(Animal other){
        if (this.getLegs() > other.getLegs()){
            return 1;
        }
        if (this.getLegs() < other.getLegs()){
            return -1;
        }
        return 0;
    }

    public void setType(String type){
        this.type = type;
    }
    public void setLegs(int legs){
        this.legs = legs;
    }
    public void setSize(int size){
        this.size = size;
    }
    public void setName(String name){
        this.name = name;
    }
    public String getType(){
        return this.type;
    }
    public int getLegs(){
        return this.legs;
    }
    public int getSize(){
        return this.size;
    }
    public String getName(){
        return this.name;
    }
    public String toString(){
        return super.toString() + "(type=" + this.getType() + ", legs=" + this.getLegs() + ", size=" + this.getSize() + ", name=" + this.getName() + ")";
    }
}
