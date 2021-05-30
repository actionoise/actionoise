<?php

$conn = mysqli_connect("HostName","user","password","DBName");
if(isset($_POST['avanti']))
{
     $SQL = "INSERT INTO pilotino (comandi) VALUES ('y')";
     $result = mysqli_query($conn,$SQL);
}
if(isset($_POST['indietro']))
{
     $SQL = "INSERT INTO pilotino (comandi) VALUES ('b')";
     $result = mysqli_query($conn,$SQL);
}
if(isset($_POST['destro']))
{
     $SQL = "INSERT INTO pilotino (comandi) VALUES ('h')";
     $result = mysqli_query($conn,$SQL);
}
if(isset($_POST['sinistro']))
{
    //$SQL="DELETE FROM pilotino";
     $SQL = "INSERT INTO pilotino (comandi) VALUES ('g')";
     $result = mysqli_query($conn,$SQL);

?>
