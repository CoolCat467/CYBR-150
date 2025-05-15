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

public class Polygon {
    private String name;
    private int sides;

    public Polygon(){
        this("untitled", 0);
    }

    public Polygon(String name, int sides){
        this.setName(name);
        this.setSides(sides);
    }

    public boolean equalTo(Polygon other){
        return this.getName().equals(other.getName()) && this.getSides() == other.getSides();
    }

    public void setName(String name){
        this.name = name;
    }
    public void setSides(int sides){
        this.sides = sides;
    }
    public String getName(){
        return this.name;
    }
    public int getSides(){
        return this.sides;
    }
    public String toString(){
        return super.toString() + "(name=\"" + this.getName() + "\", sides=" + this.getSides() + ")";
    }
}
