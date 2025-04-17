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

public class House {
    private int num_rooms;
    private int num_bathrooms;
    private int total_square_foot;
    private double current_price;

    public House(){
        this(0, 0, 0, 0.0);
    }

    public House(int num_rooms, int num_bathrooms, int total_square_foot, double current_price){
        this.setNumRooms(num_rooms);
        this.setNumBathrooms(num_bathrooms);
        this.setTotalSquareFoot(total_square_foot);
        this.setCurrentPrice(current_price);
    }

    public boolean equalTo(House other){
        return (
            this.getNumRooms() == other.getNumRooms()
            && this.getNumBathrooms() == other.getNumBathrooms()
            && this.getTotalSquareFoot() == other.getTotalSquareFoot()
            && this.getCurrentPrice() == other.getCurrentPrice()
        );
    }

    public void setNumRooms(int num_rooms){
        this.num_rooms = num_rooms;
    }
    public void setNumBathrooms(int num_bathrooms){
        this.num_bathrooms = num_bathrooms;
    }
    public void setTotalSquareFoot(int total_square_foot){
        this.total_square_foot = total_square_foot;
    }
    public void setCurrentPrice(double current_price){
        this.current_price = current_price;
    }
    public int getNumRooms(){
        return this.num_rooms;
    }
    public int getNumBathrooms(){
        return this.num_bathrooms;
    }
    public int getTotalSquareFoot(){
        return this.total_square_foot;
    }
    public double getCurrentPrice(){
        return this.current_price;
    }
    public String toString(){
        return super.toString() + "(num_rooms=" + this.getNumRooms() + ", num_bathrooms=" + this.getNumBathrooms() + ", total_square_foot=" + this.getTotalSquareFoot() + ", current_price=" + this.getCurrentPrice() + ")";
    }
}
