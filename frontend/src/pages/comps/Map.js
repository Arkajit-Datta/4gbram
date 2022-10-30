import { useJsApiLoader, GoogleMap, Marker, Autocomplete, DirectionsRenderer } from "@react-google-maps/api"

import React from "react";
import '../../style/Location.css';

const center = { lat: 17.4449, lng: 78.3498 }
const libraries = ['places'];
export default function Maps({ sourceRef, destinationRef, directionsRes }) {
    const [map, setMap] = React.useState();
    const { isLoaded } = useJsApiLoader({
        id: 'sample-map-script',
        googleMapsApiKey: "AIzaSyBRCBv1g2bhMCxviR1JYWYicWIfHyQMVCQ",
        libraries
    })

    if (!isLoaded) {
        return <>Maps Loading in Progress!</>
    }
    return (
        <div className="flex">
            <div className='inputFields'>
                <div>
                    <label>Origin :</label>
                    <Autocomplete onPlaceChanged={(e) => console.log(e)}>
                        <input ref={sourceRef} />
                    </Autocomplete>
                </div>
                <div>

                    <label>Destination :</label>
                    <Autocomplete >
                        <input ref={destinationRef} />
                    </Autocomplete>
                </div>

            </div>
            <div className="mapContainer" style={{width:'90%', margin:'0 auto'}}>
                <GoogleMap
                    onLoad={mapInstance => setMap(mapInstance)}
                    center={center} zoom={15} mapContainerStyle={{ width: '100%', height: '100%' }}
                    options={{
                        zoomControl: false,
                        streetViewControl: false,

                    }}
                >
                    {directionsRes && <DirectionsRenderer directions={directionsRes} />}

                    <Marker position={center} draggable />

                </GoogleMap>
            </div>
        </div>
    )

}