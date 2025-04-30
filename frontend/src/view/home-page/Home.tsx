import Footer from "../../components/Footer";
import CardSection from "./CardSection";
import Header from "./Header";
import InvitationToRegistration from "./InvitationToRegistration";
import PurposeSection from "./PurposeSection";

export default function Home() {
  return (
    <div>
      <Header />
      <CardSection />
      <PurposeSection />
      <InvitationToRegistration />
      <Footer />
    </div>
  )
}
