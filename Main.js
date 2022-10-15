import React from "react";
import Sidebar from "./Sidebar";
const Main = () => {
    return (

    <div>

  <div className="article">
    <h2>Main Content</h2>
    <pre>{`
    React embraces the fact that rendering logic is inherently coupled with other UI logic:
     how events are handled, how the state changes over time, and how the data is prepared for display.

    Instead of artificially separating technologies by putting markup and logic in separate files,
     React separates concerns with loosely coupled units called “components” that contain both. 
     We will come back to components in a further section, but if you’re not yet comfortable 
     putting markup in JS, this talk might convince you otherwise.
    
    React doesn’t require using JSX, but most people find it helpful as a visual aid when working
     with UI inside the JavaScript code.
     It also allows React to show more useful error and warning messages.
     function formatName(user) {
      return user.firstName + ' ' + user.lastName;
    }
    
    const user = {
      firstName: 'Harper',
      lastName: 'Perez'
    };
    
    const element = (
      <h1>
        Hello, {formatName(user)}!
      </h1>
    );
    Specifying Attributes with JSX:You may use quotes to specify string literals as attributes
    const element = <a href="https://www.reactjs.org"> link </a>;
    You may also use curly braces to embed a JavaScript expression in an attribute.
    Specifying Children with JSX:
    If a tag is empty, you may close it immediately with />, like XML:
    const element = <img src={user.avatarUrl} />;
    JSX tags may contain children.



`}
</pre>
  </div>
    <Sidebar />
    

    </div>
    
    )
};
export default Main;