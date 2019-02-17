//
//  ViewController.swift
//  hotMaps
//
//  Created by Colby Saxton on 2/16/19.
//

import UIKit
import GoogleMaps
import SwiftSocket

class ViewController: UIViewController {

    @IBOutlet weak var leadingSpace: NSLayoutConstraint!
    var menuShow = false
    @IBOutlet weak var menuView: UIView!
    var mapReference:GMSMapView? = nil
    var hs = true
    var markList = [GMSMarker]()
    
    //switches
    var userChoices : [Bool] = [true, true, true, true, true, true, true, true]
    @IBOutlet var jazzSwitch: UIView!
    @IBOutlet var hotelSwitch: UIView!
    @IBOutlet var pubSwitch: UIView!
    @IBOutlet var specialtySwitch: UIView!
    @IBOutlet var sportSwitch: UIView!
    @IBOutlet var comedySwitch: UIView!
    @IBOutlet var gamenightSwitch: UIView!
    @IBOutlet var musicSwitch: UIView!
    
    
    override func viewDidLoad() {
        super.viewDidLoad()
        // Do any additional setup after loading the view, typically from a nib.
        
        leadingSpace.constant = -225
        menuView.layer.shadowOpacity = 1
        menuView.layer.shadowRadius = 5
        
        // Create a GMSCameraPosition that tells the map to display the
        // coordinate -33.86,151.20 at zoom level 6.
        let camera = GMSCameraPosition.camera(withLatitude: 41.507050, longitude: -81.609089, zoom: 15.0)
        
        let mapView = GMSMapView.map(withFrame: UIScreen.main.bounds, camera: camera)
        mapView.center = self.view.center
        mapReference = mapView
        self.view!.addSubview(mapView)
        //view = mapView
        
        // Creates a marker in the center of the map.
        let marker = GMSMarker()
        marker.position = CLLocationCoordinate2D(latitude: -33.86, longitude: 151.20)
        marker.title = "Sydney"
        marker.snippet = "Australia"
        marker.map = mapView
        
        
        updateMarkers(mapView: mapView)
        
        _ = Timer.scheduledTimer(timeInterval: 600.0, target: self, selector: #selector(updateMarkers), userInfo: nil, repeats: true)
        
    }


    @IBAction func openMenu(_ sender: Any) {
        self.view.bringSubviewToFront(menuView)
        if(menuShow){
            leadingSpace.constant = -225
            UIView.animate(withDuration: 0.2, animations:{ self.view.layoutIfNeeded()})
            
        }
        else{
            leadingSpace.constant = 0
            UIView.animate(withDuration: 0.2, animations:{ self.view.layoutIfNeeded()})
            
            
        }
        menuShow = !menuShow
    }
    
    @objc func updateMarkers( mapView: GMSMapView){
        
        //clear the map
        //todo, clear only the ones that need to be deleted
        for var i in  0..<markList.count {
            markList[i].map = nil
        }
        
        //get the array of items
        
        let client = TCPClient(address: "127.0.0.1", port: 8000) // IP address
        
        switch client.connect(timeout: 15){
            
        case .success:
                //clear markers from map
            var result : Result
                //send query
                if self.hs {
                    result = client.send(string: "geths")
                }
                else {
                    result = client.send(string: "getevents")
                }
                
                switch result{
                case .success:
                    guard let data = client.read(1024 * 10) else {return}
                    
                    if let response = String(bytes: data, encoding: .utf8){
                        print(response)
                    }
                
                case .failure(let error):
                    print(error)
                }
            
                client.close()
        case .failure(let error):
            print(error)
            
        }
        
        //iterate through items, adding marker
        //************************************* Example marker entries
        
        addMarker(map: mapView, position: CLLocationCoordinate2D(latitude: 41.511130, longitude: -81.602635), title: "happyDog", desc: "fools gold", liveNum: 1, venueType: 1)
        
        addMarker(map: mapView, position: CLLocationCoordinate2D(latitude: 41.509197, longitude: -81.605424), title: "Sports Bar: Corner Alley" , desc: "Location: 402 Euclid Ave, Cleveland, OH 44114 \nTime: 9:00pm - 2:00am \nDescription: Come join us in the heart of downtown as we watch the final regular season game for the Cleveland Cavaliers! Defend the LAND!", liveNum: 10, venueType: 5)
        addMarker(map: mapView, position: CLLocationCoordinate2D(latitude: 41.508736, longitude: -81.604605), title: "Hotel Bar: The Vault", desc: "Location: 2017 E 9th St, Cleveland, OH 44115\nTime: 8:00pm - 2:30am \nDescription: Travel back in time and experience the glamor and luxury of a classic 1800s Cleveland bank. Surround yourself in elegance, history, and incredible hand-crafted cocktails.", liveNum: 60,  venueType: 4)
        addMarker(map: mapView, position: CLLocationCoordinate2D(latitude: 41.507441, longitude: -81.608250), title: "Music: Drag Queen Show @ The Jolly Scholar", desc: "Location: Thwing Center, 11111 Euclid Ave, Cleveland, OH 44106\nTime: 8:00pm - 10:00pm\nDescription: Catch Rupaul’s, “A Drag Queen’s Christmas” with discounted prices exclusively on Habanero! ", liveNum: 60, venueType: 3)
        addMarker(map: mapView, position: CLLocationCoordinate2D(latitude: 41.500801    , longitude: -81.592810), title: "Specialty: Fairmount Bar", desc: "Location: 2448 Fairmount Blvd, Cleveland, OH 44106\nTime: 8:00pm - 1:30am\nDescription: Enjoy Cleveland’s best made to order drinks, with over fifty beers on tap. Immerse yourself in this young and upcoming area in Cleveland Heights!", liveNum: 20, venueType: 4)
        
    }
    
    
    
    private func addMarker(map: GMSMapView, position: CLLocationCoordinate2D, title: String, desc: String, liveNum: Int, venueType: Int){
        
        var ic : UIImage
        let marker = GMSMarker(position: position)
    
        
        if userChoices[venueType] {
            marker.map = map
        }
        else{
            return;
        }

        switch(liveNum){
            //load different icon for  each venue (custom markers)
        case 0..<15:
            ic = UIImage(named: "Blue LOW Circle")!
        case 15..<40:
            ic = UIImage(named: "Orange MEDIUM circle")!
        case 40..<100:
            ic = UIImage(named: "Red HOT circle")!
        default:
            //todo error log here for a bad venue type
            ic = GMSMarker.markerImage(with: UIColor.red)
        }
        

        marker.icon = ic;
        marker.title = title
        marker.snippet = desc
        
        markList.append(marker)
    }
    
    @IBAction func jazzSwitchChanged(_ sender: Any) {
        userChoices[1] = !userChoices[1]
        updateMarkers(mapView: mapReference!)
    }
    
    @IBAction func hotelSwitchChanged(_ sender: Any) {
        userChoices[2] = !userChoices[2]
        updateMarkers(mapView: mapReference!)
    }
    
    @IBAction func pubSwitchChanged(_ sender: Any) {
        userChoices[3] = !userChoices[3]
        updateMarkers(mapView: mapReference!)
    }
    
    @IBAction func specialSwitchChanged(_ sender: Any) {
        userChoices[4] = !userChoices[4]
        updateMarkers(mapView: mapReference!)
    }
    
    @IBAction func sportSwitchChanged(_ sender: Any) {
        userChoices[5] = !userChoices[5]
        updateMarkers(mapView: mapReference!)
    }
    
    @IBAction func comedySwitchChanged(_ sender: Any) {
        userChoices[6] = !userChoices[6]
        updateMarkers(mapView: mapReference!)
    }
    
    @IBAction func gameNightSwitchChanged(_ sender: Any) {
        userChoices[7] = !userChoices[7]
        updateMarkers(mapView: mapReference!)
    }
    
    @IBAction func musicSwitchChanged(_ sender: Any) {
        userChoices[8] = !userChoices[8]
        updateMarkers(mapView: mapReference!)
    }
    
}

