import React, { useState } from "react";
import { Route, Switch, BrowserRouter } from "react-router-dom";
import Users from "./Users"
import NotFound from "./NotFound"

const Routes = () => {
    return (
        <React.Fragment>
            <BrowserRouter basename={process.env.PUBLIC_URL}>
                <Switch>
                    <Route component={Users} exact path="/users" />
                    <Route component={NotFound} />
                </Switch>
            </BrowserRouter>
        </React.Fragment>
    )
}

export default Routes;
