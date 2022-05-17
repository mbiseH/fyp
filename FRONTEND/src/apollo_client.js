import Vue from "vue";
import ApolloClient from "apollo-client";
import { HttpLink } from "apollo-link-http";
import { InMemoryCache } from "apollo-cache-inmemory";
import VueApollo from "vue-apollo";
import { BACKEND_URL } from "./settings";

Vue.use(VueApollo);

const Headers = () => {
  const headers = {};
  const token = window.localStorage.getItem("token");
  if (token) {
    headers.authorization = `jwt ${token}`;
  }
  return headers;
};

const link = new HttpLink({
  uri: BACKEND_URL,
  fetch,
  headers: Headers(),
});

const client = new ApolloClient({
  link: link,
  cache: new InMemoryCache({
    addTypename: true,
  }),
});
const apolloProvider = new VueApollo({
  defaultClient: client,
});

export default apolloProvider;
